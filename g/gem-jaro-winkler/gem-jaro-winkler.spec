%define        pkgname jaro-winkler
%define        gemname jaro_winkler

Name:          gem-%pkgname
Version:       1.5.2
Release:       alt2
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tonytonyjan/jaro_winkler
# VCS:         https://github.com/tonytonyjan/jaro_winkler.git
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
Summary:       Development files for %name
Group:         Development/Ruby

%description   devel
Development files for %{name}.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         devel
%ruby_includedir/%gemname

%files         doc
%ruby_gemdocdir

%changelog
* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2
- remove noarch from devel package
- cleanup spec

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
