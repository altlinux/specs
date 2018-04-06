# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name lzmalib
%define	major 1
%define libname lib%{name}%{major}
%define develname lib%{name}-devel

Summary: 	A thin wrapper library of LZMA
Name: 		lzmalib
Version: 	0.0.1
Release: 	alt1_10
Group: 		System/Libraries
License: 	LGPL
URL: 		http://tokyocabinet.sourceforge.net/misc/
Source0: 	http://tokyocabinet.sourceforge.net/misc/%{name}-%{version}.tar.gz
Patch0:		lzmalib-0.0.1-format_not_a_string_literal_and_no_format_arguments.diff
Patch1:		lzmalib-0.0.1-new_libname_fix.diff
BuildRequires:	chrpath
Source44: import.info

%description
This package includes a thin wrapper library of LZMA SDK written by Igor
Pavlov.

%package -n	lzmacmd
Summary:	The lzmacmd command line utility
Group:		System/Libraries

%description -n lzmacmd
This package includes the lzmacmd command line utility.

%package -n	%{libname}
Summary:	A thin wrapper library of LZMA
Group:		System/Libraries

%description -n %{libname}
This package includes a thin wrapper library of LZMA SDK written by Igor
Pavlov.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	lzmalib-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep

%setup -q
%patch0 -p0
%patch1 -p1

%build
rm configure
autoconf

%configure

%make \
    CFLAGS="%{optflags} -Wall -fPIC -fsigned-char" \
    CXXFLAGS="%{optflags} -Wall -fPIC -fsigned-char" \
    LDFLAGS="$LDFLAGS -L."

%install
%makeinstall_std

# nuke rpath
chrpath -d %{buildroot}%{_bindir}/lzmacmd


%files -n lzmacmd
%{_bindir}/lzmacmd

%files -n %{libname}
%doc README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*.a




%changelog
* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_10
- new version

* Mon Jul 28 2008 Led <led@altlinux.ru> 0.0.1-alt1
- initial build
