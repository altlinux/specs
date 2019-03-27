%define        pkgname json

Name:          ruby-%pkgname
Version:       2.2.0
Release:       alt1
Summary:       JSON parser and generator
License:       MIT
Group:         Development/Ruby
Url:           http://flori.github.io/json/
# VCS:         https://github.com/flori/json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
Obsoletes:     ruby-json-utils ruby-json-pure
Provides:      ruby-json-utils ruby-json-pure

%description
This library can parse JSON texts and generate them from ruby data
structures.


%package       devel
Summary:       Development file(s) for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   devel
Development file(s) for %gemname gem


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem


%package       -n gem-json-pure
Summary:       JSON parser and generator
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-json-pure
This library can parse JSON texts and generate them from ruby data
structures.


%package       -n gem-json-pure-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-json-pure-doc
Documentation files for %gemname gem


%prep
%setup

%build
%gem_build

%install
%gem_install

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*

%files         -n gem-json-pure
%ruby_gemspecdir/json_pure-%version.gemspec
%ruby_gemslibdir/json_pure-%version

%files         -n gem-json-pure-doc
%ruby_gemsdocdir/json_pure-%version

%changelog
* Wed Mar 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- Use Ruby Policy 2.0
- Bump to 2.2.0

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
