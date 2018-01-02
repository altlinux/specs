Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       dontpanic   
Version:    1.01
Release:    alt1_2
Summary:    Very simple library and executable used in testing Alien::Base
License:    GPL+ or Artistic    
URL:        https://perl5-alien.github.io/page/%{name}.html
Source0:    https://github.com/Perl5-Alien/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Prevent from inserting RPATH into dontpanic tool when configured with
# --disable-static option
# <https://github.com/Perl5-Alien/dontpanic/pull/3>
Patch0:     dontpanic-1.01-Do-not-force-static-linking.patch
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
%patch0 -p1
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
%doc LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_2
- new version

