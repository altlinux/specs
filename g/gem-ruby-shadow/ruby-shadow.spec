%define        pkgname ruby-shadow

Name:          gem-%pkgname
Version:       2.5.0
Release:       alt5.1
Summary:       Shadow Password module for Ruby
License:       ALT-Public-Domain or CC-PDDC
Group:         Development/Ruby
Url:           https://github.com/apalmblad/ruby-shadow
Vcs:           https://github.com/apalmblad/ruby-shadow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname < %EVR
Provides:      %pkgname = %EVR

%description
This module provides tools to read, and, on Linux, append, information
related to password files.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir


%changelog
* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt5.1
- * relicesing Free to ALT-Public-Domain

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt5
- ! spec tags and syntax
- * license

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt4
- > Ruby Policy 2.0

* Thu Nov 29 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt3
- Gemify package.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt2
- Build for aarch64.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
