# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _hardened_build 1
%global upname joedog

%define major     0
%define libname   libjoedog%{major}
%define develname libjoedog-devel

Name:           libjoedog
Version:        0.1.2
Release:        alt1_8
Summary:        Repack of the common code base of fido and siege as shared library
Group:          System/Libraries
License:        GPLv2+ and LGPLv2+
URL:            http://www.%{libname}.org/
Source0:        https://github.com/rmohr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libtool
Source44: import.info

%description
Siege is a library containing the common code base of siege and fido by Jeff
Fulmer. It consists mostly of convenience wrapper functions and a hash table
implementation.

#------------------------------------------------

%package -n     %{libname}
Summary:        Repack of the common code base of fido and siege as shared library
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

#Obsoletes:      libjoedog < 0.1.2-8

%description -n %{libname}
Siege is a library containing the common code base of siege and fido by Jeff
Fulmer. It consists mostly of convenience wrapper functions and a hash table
implementation.

#------------------------------------------------

%package -n     %{develname}
Summary:        Development package for %{name}
Group:          Development/C++
Requires:       libjoedog = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{upname}-devel = %{version}-%{release}

#Obsoletes:      libjoedog-devel < 0.1.2-8

%description -n %{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%setup -q
# old autotools want m4-dir to be present
mkdir -p m4

%build
autoreconf -vfi
%configure --disable-static
# dirty hack to force immediate binding with hardenend build having
# autocrap's libtool pass the needed ld-specs to the linker.
sed -i -e 's! \\\$compiler_flags !&%{?_hardening_ldflags} !' libtool
%make_build

%install
%makeinstall_std

install -Dpm 0644 config.h %{buildroot}%{_includedir}/%{upname}

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc README ChangeLog
%doc --no-dereference COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{version}

%files -n %{develname}
%{_includedir}/%{upname}/
%{_libdir}/%{name}.so


%changelog
* Tue Aug 22 2023 Igor Vlasenko <viy@altlinux.org> 0.1.2-alt1_8
- new version

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3
- new version

