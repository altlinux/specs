%define   pkgname json

Name:     ruby-%pkgname
Version:  2.1.0
Release:  alt2

Summary:  JSON parser and generator
License:  MIT
Group:    Development/Ruby
Url:      http://flori.github.io/json/
# VCS:    https://github.com/ruby/xmlrpc.git

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
Obsoletes: ruby-json-utils ruby-json-pure
Provides: ruby-json-utils ruby-json-pure

%description
This library can parse JSON texts and generate them from ruby data
structures.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb
rm -f {json-java,json_pure}.gemspec

%build
%ruby_config -- --use-system-libraries
%ruby_build

%install
%ruby_install
%rdoc lib/
rm -f %buildroot%_datadir/{index.html,prototype.js}
mkdir -p %buildroot%_datadir/%name
mv %buildroot%_datadir/example.json %buildroot%_datadir/%name
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
find %buildroot

%files
%ruby_sitelibdir/*
%ruby_sitearchdir/*
%rubygem_specdir/*
%_datadir/%name/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jan 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- Fixed provides and obsoletes.

* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Bump to 2.1.0

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.5.1-alt1
- [1.5.1]

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.9-alt1
- [1.1.9]

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.7-alt1
- Built for Sisyphus
