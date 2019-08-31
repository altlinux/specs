# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname octokit

Name:          gem-%pkgname
Version:       4.14.0
Release:       alt1
Summary:       Ruby toolkit for the GitHub API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/octokit/octokit.rb
%vcs           https://github.com/octokit/octokit.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         -n %pkgname
#%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1
+ packaged gem with the Ruby Policy 2.0 usage
