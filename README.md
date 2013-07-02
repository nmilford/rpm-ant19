rpm-ant19
=========

An RPM spec file to install Apache Ant 1.9.

CentOS 5 base installs Apache 1.6, which can be limiting for newer projects.

This alt-installs 1.9 beside the system 1.6 version., but makes 1.9 the default.

To call the base ant, if it is installed, you can call it directly: /usr/bin/ant

To Build: 

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget http://apache.spinellicreations.com//ant/binaries/apache-ant-1.9.1-bin.tar.gz -O ~/rpmbuild/SOURCES/apache-ant-1.9.1-bin.tar.gz`

`wget https://raw.github.com/nmilford/rpm-ant19/master/ant19.spec -O ~/rpmbuild/SPECS/ant19.spec`

`rpmbuild -bb ~/rpmbuild/SPECS/ant19.spec`
