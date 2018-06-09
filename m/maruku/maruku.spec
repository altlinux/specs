Name:    maruku
Version: 0.7.3
Release: alt1

Summary: A pure-Ruby Markdown-superset interpreter
License: MIT
Group:   Development/Ruby
Url:     https://github.com/bhollis/maruku

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Patch1:  alt-fix-data-path.patch
Patch2:  alt-remove-two-mathml-engines.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
# Remove some mathml engines support to prevent unmets
rm -f lib/maruku/ext/math/mathml_engines/{itex2mml.rb,ritex.rb}
%update_setup_rb

%build
%ruby_config --datadir=%_datadir/%name
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*
%_datadir/%name

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
