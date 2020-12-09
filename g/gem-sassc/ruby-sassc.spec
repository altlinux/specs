%define        pkgname sassc

Name:          gem-%pkgname
Version:       2.4.0
Release:       alt1.1
Summary:       Use libsass with Ruby!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sassc-ruby
Vcs:           https://github.com/sass/sassc-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch-2.2.1.patch
Patch1:        use-system-libsass.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake-compiler-dock)
BuildRequires: gem-minitest

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR
Requires:      libsass

%description
This gem combines the speed of libsass, the Sass C implementation, with
the ease of use of the original Ruby Sass library.


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
%patch1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Dec 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1.1
- ! picking up the libsass from system if any

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.2.1 -> 2.4.0

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2.1
- ! spec tags and syntax, build procedure

* Fri Nov 08 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2
- changed (*) spec to use build requires
- fixed (!) lost link to system's .so lib (closes #37433)
- fixed (!) requires

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- update (^) 2.0.0 -> 2.2.1
- use (>) Ruby Police 2.0

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.
- Disable tests.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version.
- Package as gem.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.11.4-alt1
- Initial build for Sisyphus
