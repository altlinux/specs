Name:    ruby-yui-compressor
Version: 0.12.0
Release: alt1

Summary: A Ruby interface to YUI Compressor for minifying JavaScript and CSS assets.
License: MIT and BSD-3-clause and MPL
Group:   Development/Ruby
Url:     https://github.com/sstephenson/ruby-yui-compressor/

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Ruby-YUI Compressor provides a Ruby interface to the YUI Compressor Java library for minifying JavaScript and CSS assets.

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
