
Name: speech-dispatcher
Version: 0.6.7
Release: alt5.2.1
License: %gpl2plus
Group: Sound
Summary: Speech dispatcher is a speech output processing service
URL: http://www.freebsoft.org/speechd
Packager: Michael Pozhidaev <msp@altlinux.ru>

# Automatically added by buildreq on Sun Sep 14 2008
BuildRequires: flite-devel gcc-c++ glib2-devel glibc-devel-static libalsa-devel libdotconf-devel libespeak-devel

BuildRequires: rpm-build-licenses rpm-build-python python-base python-devel

Source0: %name-%version.tar.gz

Patch1: speech-dispatcher-0.6.7-alt-flite.patch
Patch2: speech-dispatcher-0.6.7-alt-python.patch
Patch3: speech-dispatcher-0.6.7-alt-getline.patch

%add_python_req_skip speechd_config

%description
This is the Speech Dispatcher package (speech-dispatcher). It is a part of the
Free(b)soft project, which is intended to allow blind and visually impaired
people to work with computer and Internet based on free software.

%package -n libspeechd
Summary: Client library for Speech Dispatcher
Group: System/Libraries

%description -n libspeechd
Application can use this library to communicate with Speech Dispatcher service 
and produce speech output with it.

%package -n libspeechd-devel
Group: Development/C
Summary: Development files to use libspeechd to connect to Speech Dispatcher

%description -n libspeechd-devel
Application developers can use this library to connect to Speech Dispatcher daemon 
and produce speech output with it

%package -n python-module-speechd
Summary: Python client for Speech Dispatcher
Group: Development/Python

%description -n python-module-speechd
This python module allows programmers access
Speech Dispatcher service and send text data to it.

%prep
%setup -q 
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure
make

%install
%make_install DESTDIR='%buildroot' install

# This package has custom python installation via distutils setup 
# and uses /usr/lib directory even for x86_64;
if ! [ -d %buildroot%python_sitelibdir ]; then
    cp -r %buildroot/usr/lib/* %buildroot%_libdir
fi

%files
%_bindir/*
%config %_sysconfdir/%name
%_libdir/%name
%_libdir/%name-modules
%_datadir/sounds/%name
%_datadir/%name
%_infodir/*
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO

%files -n libspeechd
%_libdir/libspeechd.so.2
%_libdir/libspeechd.so.2.1.1

%files -n libspeechd-devel
%_includedir/*
%_libdir/libspeechd.so

%files -n python-module-speechd
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.7-alt5.2.1
- Rebuild with Python-2.7

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.2
- Rebuilt for soname set-versions

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.1
- Rebuilt with python 2.6

* Thu Aug 20 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt5
- 'daemon' term replaced by 'service' one (by mike@ suggestion)

* Mon Aug 17 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt4
- Applied getline patch from sbolshakov@

* Wed Aug 05 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt3
- Applied flite patch (Thanks to sbolshakov@)
- Spec cleanup (removed ldconfig and install_info calls by sbolshakov@)
- Minor fixes

* Mon Sep 15 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt2
- Fixed i586 build

* Sun Sep 07 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt1
- Initial RPM

