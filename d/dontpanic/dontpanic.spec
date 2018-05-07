Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       dontpanic   
Version:    1.02
Release:    alt1_1
Summary:    Very simple library and executable used in testing Alien::Base
License:    GPL+ or Artistic    
URL:        https://perl5-alien.github.io/page/%{name}.html
Source0:    https://github.com/Perl5-Alien/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
Source44: import.info

%description
This software provides a very simple library and executable used in testing
Alien::Base.

%package devel
Group: Other
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
This package contains libraries and header files needed for developing
applications that use %{name}.

%prep
%setup -q
autoreconf -fi

%build
%configure --enable-shared --disable-static --disable-silent-rules
%make_build

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%files
%doc --no-dereference LICENSE
%doc Changes README.md
%{_bindir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- update to new release by fcimport

* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_2
- new version

