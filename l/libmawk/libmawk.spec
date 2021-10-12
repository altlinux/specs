# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libmawk
%define major   1
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

Name:           libmawk
Version:        1.0.3
Release:        alt1_1
Summary:        Embed awk scripting language in any application written in C
Group:          System/Libraries
License:        GPLv2
URL:            http://repo.hu/projects/libmawk
Source0:        http://repo.hu/projects/libmawk/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
Source44: import.info

%description
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This provides libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.

%package -n %{libname}
Group: System/Libraries
Summary:        Library files for dynamic linking

%description -n %{libname}
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This provides libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.

%package -n %{devname}
Group: System/Libraries
Summary:        Development files
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Group: System/Libraries
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.

%prep
%setup -q


%build
export CFLAGS="%{optflags} -fcommon"
./"configure" --prefix=%{_prefix} --symbols
%make_build

%install
%makeinstall_std LIBDIR=%{buildroot}/%{_libdir} LIBARCHDIR=%{buildroot}/%{_libdir} \
              LIBPATH=%{buildroot}/%{_libdir}/%{name}

%files -n %{libname}
%doc --no-dereference src/libmawk/COPYING
%doc AUTHORS README Release_notes
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*
%{_bindir}/lmawk
%{_libdir}/%{name}/*.awk
%{_mandir}/man1/*

%files -n %{devname}
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}


%changelog
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_1
- update by mgaimport

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3
- update by mgaimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- new version

