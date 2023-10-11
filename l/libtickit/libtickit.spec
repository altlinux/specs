Group: Development/C
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global libname tickit

# Unibilium by default, otherwise ncurses
%bcond_without unibilium

Name:           lib%{libname}
Version:        0.4.3
Release:        alt1_3
Summary:        Terminal Interface Construction Kit

License:        MIT
URL:            http://www.leonerd.org.uk/code/%{name}/
Source0:        http://www.leonerd.org.uk/code/%{name}//%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  perl-devel
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Convert/Color.pm)
BuildRequires:  perl(Convert/Color/XTerm.pm)
BuildRequires:  perl(List/UtilsBy.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  pkgconfig(termkey)
%if %{with unibilium}
BuildRequires:  pkgconfig(unibilium) >= 1.1.0
%else
BuildRequires:  libncurses++-devel libncurses++w-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
%endif
# Tests
BuildRequires:  %{_bindir}/prove
Source44: import.info

%description
This library provides an abstracted mechanism for building interactive
full-screen terminal programs. It provides a full set of output drawing
functions, and handles keyboard and mouse input events.

%package -n libtickit3
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n libtickit3
This library provides an abstracted mechanism for building interactive
full-screen terminal programs. It provides a full set of output drawing
functions, and handles keyboard and mouse input events.

This package contains the shared library.

%package devel
Group: Development/C
Summary:        Development files needed for %{name}
Requires:       libtickit3 = %EVR
%if %{with unibilium}
%endif

%description devel
%{summary}.

%prep
%setup -q

rm -f src/linechars.inc src/xterm-palette.inc
rm -f t/11term-output-screen.*

%build
CFLAGS="%{optflags}"  %{make_build} VERBOSE=1

%install
%{makeinstall_std} PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
CFLAGS="%{optflags} -D_XOPEN_SOURCE"  make test VERBOSE=1
make examples

%files -n libtickit3
%doc --no-dereference LICENSE
%doc CHANGES examples README.md
%_libdir/libtickit.so.3
%_libdir/libtickit.so.3.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_includedir}/%{libname}-*.h
%{_libdir}/pkgconfig/%{libname}.pc
%{_mandir}/man3/%{libname}_*.3*
%{_mandir}/man7/%{libname}.7*
%{_mandir}/man7/%{libname}_*.7*

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.4.3-alt1_3
- update to new release by fcimport

* Wed Nov 24 2021 Igor Vlasenko <viy@altlinux.org> 0.4.2a-alt1_1
- new version

