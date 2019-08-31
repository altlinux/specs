%define        pkgname benchmark_suite

Name: 	       ruby-%pkgname
Version:       1.0.0
Release:       alt2.git5bded6.1
Summary:       A set of enhancements to the standard library benchmark.rb
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evanphx/benchmark_suite
%vcs           https://github.com/evanphx/benchmark_suite.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit)
BuildRequires: gem(benchmark-ips)
BuildRequires: gem(hoe)

%gem_replace_version benchmark-ips ~> 2.0
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This package contains a command line tool for running multiple
benchmarks against multiple rubies. It is also uses benchmark/ips to
report iterations per second.


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
%_bindir/benchmark
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2.git5bded6.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6.1
- Rebuild with new Ruby autorequirements.

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6
- Initial build for ALT Linux
