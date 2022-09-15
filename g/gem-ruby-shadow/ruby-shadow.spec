%define        gemname ruby-shadow

Name:          gem-ruby-shadow
Version:       2.5.1
Release:       alt1
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
Obsoletes:     ruby-shadow < %EVR
Provides:      ruby-shadow = %EVR
Provides:      gem(ruby-shadow) = 2.5.1


%description
This module provides tools to read, and, on Linux, append, information related
to password files.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README README.euc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- ^ 2.5.0 -> 2.5.1

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
