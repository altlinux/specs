Name: ruby-fcgi
Version: 0.9.2.1
Release: alt2

Summary: FastCGI for ruby
Group: Development/Ruby
License: Ruby
Url: https://github.com/alphallc/ruby-fcgi-ng

BuildRequires: libfcgi-devel libruby-devel ruby-tool-setup

Source: %name-%version.tar

%description
FastCGI is a language independent, scalable, open extension to CGI
that provides high performance without the limitations of server
specific APIs.

MoonWolf developed a library for FastCGI in
http://www.moonwolf.com/ruby/archive/. But now, he is MIA.

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README*
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2
- Rebuild with new %%ruby_sitearchdir location

* Thu Sep 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt1
- New version 0.9.2.1

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.8.8-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.8.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.8-alt1
- [0.8.8]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Rebuilt with Ruby 1.9

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 0.8.7-alt1
- [0.8.7]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.6-alt1
- first build
