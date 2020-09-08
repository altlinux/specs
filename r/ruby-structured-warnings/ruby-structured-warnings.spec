%define        pkgname structured-warnings
%define        gemname structured_warnings

Name:          ruby-%pkgname
Version:       0.4.0
Release:       alt1
Summary:       This is an implementation of Daniel Berger's proposal of structured warnings for Ruby.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/schmidt/structured_warnings
%vcs           https://github.com/schmidt/structured_warnings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
This is an implementation of Daniel Berger's proposal of structured warnings for
Ruby. They provide dynamic suppression and activation, as well as, an
inheritance hierarchy to model their relations. This library preserves the old
warn signature, but additionally allows a raise-like use.


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
* Tue Sep 08 2020 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- New version.

* Wed Jul 31 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt2
% Ruby Policy 2.0

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
