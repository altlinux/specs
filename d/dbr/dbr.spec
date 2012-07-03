%def_disable backport_M4x
Name: dbr
Version: 0.1.1
Release: alt1.1.1

Summary: Daisy Book Reader
Summary(ru_RU.UTF-8): Утилита для чтения книг в формате Daisy
License: %gpl3only
Packager: Michael Pozhidaev <msp@altlinux.ru>
Group: Accessibility
URL: http://sourceforge.net/project/showfiles.php?group_id=233851

# Automatically added by buildreq on Sat Dec 27 2008
BuildRequires: intltool python-devel python-module-gst

BuildRequires: rpm-build-licenses python-module-pygtk

Source0: %name-%version.tar.gz

%description
DBR is an application for accessing and reading books in the Daisy 2.02 standard. Although Daisy 3.0 is not supported.
Daisy books are also known as DTB's (Digital/Daisy Talking Books.

%description -l ru_RU.UTF-8
DBR - это утилита для чтения говорящих книг в формате Daisy. В
настоящий момент поддерживаются Daisy книги версии формата 2.2. 
Поддержка Daisy 3.0 в настоящий момент находится в процессе
разработки.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%if_enabled backport_M4x
%post
%update_menus
%endif

%if_enabled backport_M4x
%postun
%clean_menus
%endif

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING INSTALL MAINTAINERS NEWS README
%_bindir/*
%dir %python_sitelibdir/%name
%python_sitelibdir/%name
%_datadir/applications/*

%changelog
* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.1
- Rebuilt with python 2.6

* Sat Dec 27 2008 Michael Pozhidaev <msp@altlinux.ru> 0.1.1-alt1
- Initial package for Sisyphus

* Wed Jul 16 2008 Francisco Javier Dorado <javier@tiflolinux.org>
- First attempt to create this file.

