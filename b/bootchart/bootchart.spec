# sometimes spec file was here: http://prdownloads.sourceforge.net/bootchart/bootchart-0.9-1.src.rpm ...

%define section free

Name: bootchart
Version: 0.9
Release: alt1_2jpp5
Summary: Boot Process Performance Visualization
License: GPL
Url: http://www.bootchart.org/
Packager: Eugeny A. Rostovtsev (REAL) <real@altlinux.org>

Source: http://www.bootchart.org/dist/SOURCES/%name-%version.tar.bz2
Group: Monitoring
#BuildRequires(pre): jpackage-utils
BuildRequires(pre): rpm-build-java
BuildRequires(pre): java-devel-default

# Automatically added by buildreq on Mon Dec 29 2008
#BuildRequires: ant jakarta-commons-cli java-1.6.0-sun-accessibility tzdata

BuildRequires: ant tzdata
BuildRequires: jakarta-commons-cli >= 0:1.0

BuildArch: noarch

%description
A tool for performance analysis and visualization of the GNU/Linux boot
process. Resource utilization and process information are collected during
the boot process and are later rendered in a PNG, SVG or EPS encoded chart.

%package javadoc
Summary: Javadoc for bootchart
Group: Development/Documentation

%description javadoc
Javadoc for bootchart.

%package logger
Summary: Boot logging script for bootchart
Group: System/Configuration/Boot and Init
Requires: %name = %version-%release

%define boottitle "Bootchart logging"

%description logger
Boot logging script for bootchart.

%prep
%setup

%build
# Remove the bundled commons-cli
#rm -rf lib/org/apache/commons/cli lib/org/apache/commons/lang
#export CLASSPATH=$(build-classpath commons-cli ant)
sed -i -e 's/\/var\/log/\/var\/log\/%name/g' src/org/%name/Main.java*
sed -i -e 's/\/var\/log/\/var\/log\/%name/' script/%{name}d.conf
%ant

%install
mkdir -p %buildroot%_var/log/%name
# jar
install -D -m 644 %name.jar %buildroot%_javadir/%name-%version.jar
ln -s %name-%version.jar %buildroot%_javadir/%name.jar

# script
install -D -m 755 script/%name %buildroot%_bindir/%name

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name-%version
cp -pr javadoc/* %buildroot%_javadocdir/%name-%version
ln -s %name-%version %buildroot%_javadocdir/%name # ghost symlink

# logger
install -D -m 755 script/%{name}d %buildroot%_sbindir/%{name}d
install -D -m 644 script/%{name}d.conf %buildroot%_sysconfdir/%{name}d.conf

sed -i '1s|/sh|/bash|' %buildroot%_sbindir/%{name}d

%post javadoc
rm -f %_javadocdir/%name
ln -s %name-%version %_javadocdir/%name

%post logger
# Add a new grub/lilo entry
if [ -x /sbin/grubby ]; then
        kernel=$(grubby --default-kernel)
        initrd=$(grubby --info=$kernel | sed -n '/^initrd=/{s/^initrd=//;p;q;}')
        [ ! -z $initrd ] && initrd="--initrd=$initrd"
        grubby --remove-kernel TITLE=%boottitle
        grubby --copy-default --add-kernel=$kernel $initrd --args="init=/sbin/%{name}d" --title=%boottitle
fi

%preun logger
# Remove the grub/lilo entry
if [ -x /sbin/grubby ]; then
	grubby --remove-kernel TITLE=%boottitle
fi

%files
%doc ChangeLog COPYING INSTALL README TODO lib/LICENSE.cli.txt
%doc lib/LICENSE.compress.txt lib/LICENSE.epsgraphics.txt lib/NOTICE.txt
%_javadir/*
%_bindir/%name
%_var/log/%name

%files javadoc
%doc %_javadocdir/%name-%version
%doc %_javadocdir/%name

%files logger
%doc README.logger
%_sbindir/%{name}d
%config(noreplace) %_sysconfdir/%{name}d.conf

%changelog
* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1_2jpp5
- Fixed for checkbashisms

* Mon Jan 05 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.9-alt1_1jpp5
- First build for Sisyphus

