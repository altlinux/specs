Name:    ruby-libvirt
Version: 0.7.1
Release: alt1.1

Summary: Ruby bindings for libvirt
License: LGPLv2+
Group:   Development/Ruby
Url:     http://libvirt.org/ruby/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libvirt-devel >= 0.4.0

%description
Ruby bindings for libvirt.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %{name}.

%prep
%setup -q
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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
Initial build for Sisyphus.
