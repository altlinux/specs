%define        pkgname bones

Name:          gem-%pkgname
Version:       3.8.4
Release:       alt1
Summary:       Mr Bones is a handy tool that creates new Ruby projects from a code skeleton
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/bones
Vcs:           https://github.com/TwP/bones.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%gem_replace_version rdoc ~> 6.0
%gem_replace_version rake ~> 13.0

%description
%summary. The skeleton contains some starter code and a collection of rake tasks
to ease the management and deployment of your source code. Several Mr Bones
plugins are available for creating git repositories, creating GitHub projects,
running various test suites and source code analysis tools.


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
* Tue Jun 30 2020 Pavel Skrylev <majioa@altlinux.org> 3.8.4-alt1
- + packaged as a gem with usage Ruby Policy 2.0.
