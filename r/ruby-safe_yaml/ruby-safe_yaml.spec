
Name:    ruby-safe_yaml
Version: 1.0.4
Release: alt1

Summary: Parse YAML safely
Group:   Development/Ruby
License: MIT
URL: 	 https://github.com/tenderlove/rexical

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby 
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-setup

Source: %name-%version.tar

%description
The SafeYAML gem provides an alternative implementation of
YAML.load suitable for accepting user input in Ruby applications.
Unlike Ruby's built-in implementation of YAML.load, SafeYAML's
version will not expose apps to arbitrary code execution exploits.

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
%ruby_test_unit -Ilib:ext:test tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README.md
%ruby_sitelibdir/*

%files doc
%doc CHANGES.md
%ruby_ri_sitedir/SafeYAML/*
%ruby_ri_sitedir/YAML/*

%changelog
* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux
