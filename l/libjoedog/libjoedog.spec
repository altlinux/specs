# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _hardened_build 1
%global libname joedog
%global current 0

Name:           lib%{libname}
Version:        %{current}.1.2
Release:        alt1_3
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


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
%{summary}.


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
%make

%install
%makeinstall_std

install -Dpm 0644 config.h %{buildroot}%{_includedir}/%{libname}
rm -f %{buildroot}%{_libdir}/%{name}.la

%files
%doc README ChangeLog COPYING
%{_libdir}/%{name}.so.%{current}
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/%{libname}
%{_libdir}/%{name}.so


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3
- new version

