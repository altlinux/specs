Name: tsung
Version: 1.7.0
Release: alt1
Summary: A distributed multi-protocol load testing tool
URL: http://%name.erlang-projects.org/
License: %gpl2plus
Group: Development/Tools
Source: http://%name.erlang-projects.org/dist/%name-%version.tar
BuildArch: noarch
Provides: erlang-%name = %version-%release
Requires: erlang-otp  perl-RRD
Packager: hsv <hsv@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-erlang
BuildRequires: rpm-build-erlang
BuildRequires: erlang-otp-devel
BuildRequires: perl-RRD perl-JSON

%description
%name is a distributed load testing tool. It is protocol-independent
and can currently be used to stress and benchmark HTTP and Jabber
servers. It simulates user behaviour using an XML description file,
reports many measurements in real time (statistics can be customized
with transactions, and graphics generated using gnuplot).
For HTTP, it supports 1.0 and 1.1, has a proxy mode to record sessions,
supports GET and POST methods, Cookies, and Basic WWW-authentication.
It also has support for SSL.


%prep
%setup


%build
%autoreconf
%configure
%make_build %name doc
%make
bzip2 --best --keep --force CHANGELOG.md


%install
%make_install \
    DESTDIR=%buildroot \
    PACKAGE_TARNAME=%name-%version \
    DOC_DIR=%_docdir/%name-%version \
    ERLANG_LIB_DIR=%_otplibdir \
    LIBDIR=%_libexecdir/%name \
    install
rm -rf %buildroot%_otplibdir/{*/{src,BUILD_OPTIONS},tsung_*/include}
install -m 0644 CHANGELOG* CONTRIBUTORS README.md TODO  %buildroot%_docdir/%name-%version/


%files
%_docdir/%name-%version/*
%_bindir/*
#%_otplibdir/*
%_man1dir/*
%_libexecdir/%name
%_datadir/%name


%changelog
* Tue Oct 31 2017 Denis Medvedev <nbr@altlinux.org> 1.7.0-alt1
- new version

* Mon Oct 23 2017 Denis Medvedev <nbr@altlinux.org> 1.6.0-alt1.1
- Rebuild with fixed rpm-build-erlang.

* Thu Apr 07 2016 Denis Medvedev <nbr@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Wed Apr 06 2016 Denis Medvedev <nbr@altlinux.org> 1.4.1.git20111220-alt1.2
- removed strict requirement for erlang build system

* Tue Apr 05 2016 Denis Medvedev <nbr@altlinux.org> 1.4.1.git20111220-alt1.1
- removed strict requirement for erlang version.

* Tue Dec 27 2011 Sergey Shilov <hsv@altlinux.org> 1.4.1.git20111220-alt1
- 1.4.1.git20111220
- use upstream git repository
- Erlang R15B ready

* Mon Feb 02 2009 Led <led@altlinux.ru> 1.3.0-alt1
- 1.3.0
- fixed Group

* Sat Aug 16 2008 Led <led@altlinux.ru> 1.2.2-alt2
- update BuildRequires
- added %name-1.2.2-alt.patch

* Thu Mar 06 2008 Led <led@altlinux.ru> 1.2.2-alt1
- 1.2.2
- updated %name-1.2.2-makefile.patch

* Sat Feb 16 2008 Led <led@altlinux.ru> 1.2.1-alt2
- fixed spec

* Wed Jul 11 2007 Led <led@altlinux.ru> 1.2.1-alt1
- initial build for Sisyphus
- cleaned up spec
- fixed License
- added %name-1.2.1-makefile.patch

* Wed Sep 20 2006 Nicolas Niclausse <Nicolas.Niclausse@sophia.inria.fr> 1.2.1-1
- update 'requires': erlang (as in fedora extra) instead of erlang-otp

* Wed Apr 27 2005 Nicolas Niclausse <nicolas.niclausse@niclux.org> 1.0.2-1
- new release

* Thu Nov  18 2004 Nicolas Niclausse <nicolas.niclausse@niclux.org> 1.0.1-1
- new release

* Mon Aug  9 2004 Nicolas Niclausse <nicolas.niclausse@IDEALX.com> 1.0-1
- new release

* Mon Aug  9 2004 Nicolas Niclausse <nicolas.niclausse@IDEALX.com> 1.0.beta7-2
- fix doc 

* Mon Aug  9 2004 Nicolas Niclausse <nicolas.niclausse@IDEALX.com> 1.0.beta7-1
- initial rpm 
