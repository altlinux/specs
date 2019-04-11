Name:    puma
Version: 3.12.1
Release: alt1

Summary: A Ruby/Rack web server built for concurrency
License: BSD 3-Clause
Group:   Development/Ruby
Url:     https://github.com/puma/puma

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel
BuildRequires: rake-compiler
# For tests
#BuildRequires: gem(rack)

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server
for Ruby/Rack applications in development and production.

%package -n gem-puma
Summary: A Ruby/Rack web server built for concurrency (gem)
Group:   Development/Ruby

%description -n gem-puma
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server
for Ruby/Rack applications in development and production.

This is the gem for puma executable.

%package devel
Summary: Development files for %name
Group: Development/Documentation
BuildArch: noarch

%description devel
Development files for %name.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version

%build
%gem_build

%install
%gem_install

%check
#gem_test

%files
%doc README*
%_bindir/%{name}*

%files -n gem-puma
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files devel
%ruby_includedir/*

%files doc
%ruby_gemdocdir

%changelog
* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.12.1-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- New version.
- Package according to Ruby Policy 2.0

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt2
- Package as gem.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1
- Initial build for Sisyphus
