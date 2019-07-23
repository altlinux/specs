%define        pkgname ruby-shadow
%define        gemname ruby-shadow

Name: 	       %pkgname
Version:       2.5.0
Release:       alt4
Summary:       Shadow Password module for Ruby
License:       Public Domain License
Group:         Development/Ruby
Url:           https://github.com/apalmblad/ruby-shadow
%vcs           https://github.com/apalmblad/ruby-shadow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

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
* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt4
- Use Ruby Policy 2.0

* Thu Nov 29 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt3
- Gemify package.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt2
- Build for aarch64.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
