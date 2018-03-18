# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 8
%define libname libticonv%{major}
%define develname libticonv-devel

Name:           libticonv
Version:        1.1.5
Release:        alt1_1
Summary:        Texas Instruments calculators charsets library
Group:          System/Libraries
License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        https://download.sourceforge.net/tilp/%{name}-%{version}.tar.bz2
BuildRequires:  glib2-devel
Source44: import.info

%package -n %{libname}
Group:          System/Libraries
Summary:        Texas Instruments calculators charsets library
Provides:       %{name} = %{version}-%{release}

%package -n %{develname}
Group:          Development/C
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description
The ticonv library is a library capable of conversions between
Texas Instruments character sets and UTF-8/UTF-16 character sets.

%description -n %{libname}
The ticonv library is a library capable of conversions between
Texas Instruments character sets and UTF-8/UTF-16 character sets.

%description -n %{develname}
Include files and libraries for linking and developing
applications using libticonv.

%prep
%setup -q

# Fix wrong EOF encodings.
sed -i 's/\r$//' \
        README \
        ChangeLog \
        AUTHORS \
        docs/html/clean.bat \
        docs/html/style.css

#silence autoreconf warning
mkdir -p m4

%build
autoreconf -vfi
%configure \
	--disable-static \
	--enable-iconv
%make_build

%check
make check

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

#handle docs in files section
rm -rf %{buildroot}%{_docdir}

%files -n %{libname}
%doc README AUTHORS ChangeLog
%{_libdir}/libticonv.so.%{major}
%{_libdir}/libticonv.so.%{major}.*

%files -n %{develname}
%doc docs/html/
%doc docs/charsets/
%{_libdir}/libticonv.so
%{_libdir}/pkgconfig/ticonv.pc
%{_includedir}/tilp2/


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_1
- new version

