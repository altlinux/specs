%define        pkgname jaro-winkler
%define        gemname jaro_winkler

Name:          gem-%pkgname
Version:       1.5.3
Release:       alt1.1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string
Summary(ru_RU.UTF-8): Воплощение алгоритма расстояний Яро-Винклера на Си и Рубине, который поддерживает строки UTF-8
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tonytonyjan/jaro_winkler
%vcs           https://github.com/tonytonyjan/jaro_winkler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(minitest)

%description
jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.


%package       devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         devel
%ruby_includedir/%gemname

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1.1
- ! spec according to changelog rules

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1
- ^ v1.5.3
- ! spec

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2
- remove noarch from devel package
- cleanup spec

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
