Name: ruby-fcgi
Version: 0.8.8
Release: alt1

Summary: FastCGI for ruby
Group: Development/Ruby
License: Ruby
Url: http://rubyforge.org/projects/fcgi/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

# Automatically added by buildreq on Wed Apr 02 2008 (-bi)
BuildRequires: libfcgi-devel libruby-devel ruby-tool-setup

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
FastCGI is a language independent, scalable, open extension to CGI 
that provides high performance without the limitations of server 
specific APIs.

MoonWolf developed a library for FastCGI in 
http://www.moonwolf.com/ruby/archive/. But now, he is MIA. 

%prep
%setup -q
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%ruby_sitelibdir/*
%ruby_sitearchdir/*
%doc README README.signals

%changelog
* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.8-alt1
- [0.8.8]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Rebuilt with Ruby 1.9

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 0.8.7-alt1
- [0.8.7]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.6-alt1
- first build
