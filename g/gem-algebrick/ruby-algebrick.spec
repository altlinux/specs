%define        pkgname algebrick

Name:          gem-%pkgname
Version:       0.7.5.1
Release:       alt0.1
Summary:       Typed structs on steroids based on algebraic types and pattern matching.
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/pitr-ch/algebrick
Vcs:           https://github.com/pitr-ch/algebrick.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %version.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Typed structs on steroids based on algebraic types and pattern matching
seamlessly integrating with standard Ruby features.


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
%patch -p1

%build
%ruby_build --use=%gemname --version-replace=%version

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
* Thu Feb 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.5.1-alt0.1
- ! fake class matching when it uses changed or mimic name
- ^ 0.7.5 -> 0.7.5[1]

* Tue Feb 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt2
- > Ruby Policy 2.0
- * policify name

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- Initial build for Sisyphus
