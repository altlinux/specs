Name: expedite
Version: 1.2.0
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Evas benchmark tool
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

# http://svn.enlightenment.org/svn/e/trunk/%name
Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: gcc-c++
BuildRequires: libevas-devel >= 1.2.0
BuildRequires: libeina-devel >= 1.2.0
BuildRequires: libeet-devel >= 1.6.0
BuildRequires: libX11-devel

%description
Expedite is the official Evas benchmark tool. It can test different
engines, such as X11, XRender, OpenGL (also ES variant), SDL, DirectFB
and so on. Its tests are quite extensive, trying to reproduce real world
usage cases.

%prep
%setup -q -n %name-%version

%build
%configure
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_datadir/%name/
%doc AUTHORS COPYING* README

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus

