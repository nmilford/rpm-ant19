# To Build: 
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget http://apache.spinellicreations.com//ant/binaries/apache-ant-1.9.1-bin.tar.gz -O ~/rpmbuild/SOURCES/apache-ant-1.9.1-bin.tar.gz
# wget https://raw.github.com/nmilford/rpm-ant19/master/ant19.spec -O ~/rpmbuild/SPECS/ant19.spec
# rpmbuild -bb ~/rpmbuild/SPECS/ant19.spec

Name:           ant19
Version:        1.9.1
Release:        1
Summary:        Ant build tool for Java
License:        Apache Software License
URL:            http://ant.apache.org/
Group:          Development/Build Tools
Source0:        apache-ant-%{version}-bin.tar.gz
Requires:       jdk
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ant is a platform-independent build tool for java. 

CentOS 5 base installs Apache 1.6, which can be limiting for newer projects.

This alt-installs 1.9 beside the system 1.6 version., but makes 1.9 the default.

%prep
%setup -q -n apache-ant-%{version}

%build

install -d -m 755 %{buildroot}/opt/%{name}
cp -R %{_builddir}/apache-ant-%{version}/* %{buildroot}/opt/%{name}/

# Make it the default, dawg.
install -d -m 755 %{buildroot}/etc/profile.d/
%{__cat} <<EOF > %{buildroot}/etc/profile.d/%{name}.sh
export ANT_HOME=/opt/%{name}
export PATH=/opt/%{name}/bin:$PATH
EOF

%clean
rm -rf %{buildroot}

%post
echo "You will need to exit your shell to have ant in your default path."
echo "Or run the following"
echo '  export ANT_HOME=/opt/ant19'
echo '  export PATH=/opt/ant19/bin:$PATH'
echo
echo "To call the base ant, if it is installed, you can call it directly: /usr/bin/ant"


%files
/opt/%{name}/
/etc/profile.d/%{name}.sh

%changelog
* Sun Jun 30 2013 Nathan Milford <nathan@milford.io> - 1.9.1-1
- First go at it.