Name: ccafe-gui
Version: 0.5.7
Release: alt1.svn20090721
Summary: GUI for Ccaffeine framework
License: LGPL
Group: Networking/Other
Url: http://www.cca-forum.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.pythonpaste.org/Paste/WSGIFilter/trunk
Source: %name-%version.tar.gz

Requires: ccaffeine babel

BuildRequires(pre): rpm-build-java
BuildPreReq: java-devel-default ant babel ccaffeine zip

%description
GUI for the Common Component Architecture Framework compliant with the
CCA specification.

%package javadoc
Summary: Javadoc for ccafe-gui
Group: Development/Documentation
BuildArch: noarch

%description javadoc
GUI for the Common Component Architecture Framework compliant with the
CCA specification.

This package contains Javadoc for ccafe-gui.

%prep
%setup

%build
%autoreconf
%configure \
	--with-ccafe-config=%_bindir/ccafe-config
%make_build

%ant docs

%install
install -d %buildroot%prefix
%makeinstall_std

install -d %buildroot%_javadir
mv %buildroot%_libexecdir/*.jar %buildroot%_javadir/
mv %buildroot%_libexecdir/*.sh %buildroot%_bindir/
sed -i 's|\./\(ccafe\-gui\.jar\)|%_javadir/\1|g' \
	%buildroot%_bindir/simple-gui.sh
sed -i 's|\$INSTALLATION/lib/\(ccafe\-gui\.jar\)|%_javadir/\1|g' \
	%buildroot%_bindir/gui.sh

install -d %buildroot%_javadocdir/%name-%version
cp -fR docs/* %buildroot%_javadocdir/%name-%version/

%files
%doc CHANGES README
%_bindir/*
%_javadir/*

%files javadoc
%_javadocdir/%name-%version

%changelog
* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt1.svn20090721
- Initial build for Sisyphus

