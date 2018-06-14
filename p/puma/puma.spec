Name:    puma
Version: 3.11.4
Release: alt1

Summary: A Ruby/Rack web server built for concurrency
License: BSD 3-Clause
Group:   Development/Ruby
Url:     https://github.com/puma/puma

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
# For tests
#BuildRequires: ruby-rack

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server
for Ruby/Rack applications in development and production.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%%ruby_test_unit -Ilib:ext:test test

%files
%doc README*
%_bindir/%{name}*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1
- Initial build for Sisyphus
