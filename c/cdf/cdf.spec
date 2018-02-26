Summary: colorized df
Name: cdf
Version: 0.2
Release: alt1
Source0: %{name}-%{version}.tar.gz
URL: http://bmp-plugins.berlios.de/misc/cdf/cdf.html
License: GPL
Group: Monitoring

%description
cdf is a tool simular to df(1), but with colors support. Note that 
cdf is _not_ just df with colors and it doesn't compatible with df 
(however, compatiblity with df may be realized later).

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%doc README AUTHORS NEWS TODO

%changelog
* Fri Jan 27 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.2-alt1
- 0.2

* Thu Nov 04 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1-alt1
- Implementation build

