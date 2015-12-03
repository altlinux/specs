Name: macchanger
Version: 1.5
Release: alt1.qa1.1

Summary: utility for viewing/manipulating the MAC address of network interfaces
License: GPL v2+
Group: Networking/Other
Url: http://www.alobbs.com/macchanger
Packager: Maxim Ivanov <redbaron@altlinux.org>

Source: %url/%name-%version.tar
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Features:
- Set specific MAC address of a network interface
- Set the MAC randomly
- Set a MAC of another vendor
- Set another MAC of the same vendor
- Set a MAC of the same kind (eg: wireless card)
- Display a vendor MAC list (today, 6800 items) to choose from
%prep
%setup

%build
#%autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%_datadir/%name
%_man1dir/*
%_infodir/*
#%_sbindir/*
#%doc %_docdir/*

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1.qa1.1
- NMU: added BR: texinfo

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Mar 01 2009 Maxim Ivaniv <redbaron at altlinux.org> 1.5-alt1
- Initial build for Sisyphus 

