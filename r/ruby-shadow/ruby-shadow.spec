Name:    ruby-shadow
Version: 2.5.0
Release: alt2

Summary: Shadow Password module for Ruby
License: Public Domain License
Group:   Development/Ruby
Url:     https://github.com/apalmblad/ruby-shadow

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%description
This module provides tools to read, and, on Linux, append, information
related to password files.

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
ruby extconf.rb
%make_build

%install
%makeinstall_std
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt2
- Build for aarch64.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
