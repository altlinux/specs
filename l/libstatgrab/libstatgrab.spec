BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(IPC/Cmd.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define shortname	statgrab
%define major		10
%define libname		lib%{shortname}%{major}
%define libnamedevel	lib%{shortname}-devel

Name:		libstatgrab
Version:	0.92.1
Release:	alt1_1
Summary:	Make system statistics
License:	LGPLv2+ and GPLv2+
Group:		Monitoring
URL:		https://www.i-scream.org/libstatgrab/
Source0:	ftp://ftp.uk.i-scream.org/pub/i-scream/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}.nochmod.patch
BuildRequires:	pkgconfig(ncurses)
Source44: import.info


%description
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more.

The current list of platforms is Solaris 2.x, Linux, and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible.

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab.

%package -n	%{shortname}-tools
Summary:	Tools from %{name} to monitoring the system
Group:		Monitoring
License:	GPLv2+

%description -n %{shortname}-tools
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more.

The current list of platforms is Solaris 2.x, Linux , and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible.

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab.

%package -n	%{libname}
Summary:	The %{name} libraries
Group:		System/Libraries
License:	LGPLv2+
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{libnamedevel}
Summary:	The development files from %{name} libraries
Group:		Development/Other
License:	LGPLv2+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{libnamedevel}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0


%build
%configure --disable-static
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

rm -rf %{buildroot}%{_docdir}/%{name}
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin,/usr/games} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files -n %{shortname}-tools
%doc AUTHORS README ChangeLog NEWS
%{_bindir}/saidar
%{_bindir}/%{shortname}*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%doc AUTHORS README ChangeLog NEWS
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{libnamedevel}
%doc AUTHORS README ChangeLog NEWS
%{_libdir}/%{name}.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.92.1-alt1_1
- update by mgaimport

* Wed Jan 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_3
- update by mgaimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_1
- update by mgaimport

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_1
- new version; new maintainer

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.1
- Removed bad RPATH

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 0.17-alt1
- NMU: 0.17 (thx fedorawatch)

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.qa1.1
- Rebuilt for soname set-versions

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.16-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libstatgrab
  * postun_ldconfig for libstatgrab
  * postclean-05-filetriggers for spec file

* Mon May 25 2009 Sergey Zhumatiy <zhum@altlinux.org> 0.16-alt1
- fixed wrong pkgconfig file location on x86_64 (spec file bug)
- new version 0.16
- saidar is added as separated package

* Thu Nov 15 2007 Sergey Zhumatiy <zhum@altlinux.org> 0.14-alt3
- saidar deleted from package because of unstable compiling

* Fri Oct 19 2007 Sergey Zhumatiy <zhum@altlinux.org> 0.14-alt2
- main pakage is splitted to libstatgrab and libstatgrab-tools

* Fri Oct 05 2007 Sergey Zhumatiy <zhum@altlinux.org> 0.14-alt1
- initial build

