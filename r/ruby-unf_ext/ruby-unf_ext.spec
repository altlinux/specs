%define        pkgname unf-ext
%define        gemname unf_ext

Name: 	       ruby-%gemname
Version:       0.0.7.5
Release:       alt2
Summary:       Unicode Normalization Form support library for CRuby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-unf_ext
# VCS:         https://github.com/knu/ruby-unf_ext.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++

%description
%summary


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.7.5-alt2
- Use Ruby Policy 2.0

* Wed Aug 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.3
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.0.M80P.1
- Rebuild with Ruby 2.4.2

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.1
- Rebuild with Ruby 2.4.2

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1
- Initial build for Sisyphus.
