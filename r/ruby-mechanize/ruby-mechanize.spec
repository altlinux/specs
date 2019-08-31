# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname mechanize

Name:          ruby-%pkgname
Version:       2.7.6
Release:       alt1
Summary:       WWW::Mechanize, a handy web browsing ruby object
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/sparklemotion/mechanize
%vcs           https://github.com/sparklemotion/mechanize.git
Source:        %name-%version.tar

BuildArch:     noarch
BuildRequires(pre): rpm-build-ruby

%description
The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects,
can follow links, and submit forms.  Form fields can be populated and
submitted.  Mechanize also keeps track of the sites that you have visited as
a history.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- Bump to 2.7.66
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1.4
- Rebuild with new Ruby autorequirements.

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.3-alt1.3
- fixed encoding without iconv

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.3-alt1.2
- don't use iconv for ruby >= 1.9.2

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.9.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- build for Sisyphus

