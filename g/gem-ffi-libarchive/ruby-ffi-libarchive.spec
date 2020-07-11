%define        pkgname ffi-libarchive

Name:          gem-%pkgname
Version:       1.0.3
Release:       alt1
Summary:       A Ruby FFI binding to libarchive.
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/chef/ffi-libarchive
Vcs:           https://github.com/chef/ffi-libarchive.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

This library provides Ruby FFI bindings to the well-known libarchive library.


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
* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- > Ruby Policy 2.0
- ^ 0.4.2 -> 1.0.3

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- New version.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
