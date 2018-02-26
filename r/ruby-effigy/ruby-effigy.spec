# vim: set ft=spec: -*- rpm-spec -*-

%define plugname effigy

Name: ruby-%plugname
Version: 0.3.1
Release: alt1

Summary: Ruby views without a templating language
License: MIT
Group: Development/Ruby
Url: http://github.com/jferris/effigy

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

PreReq: ruby-railties >= 2.1.0-alt2

# Automatically added by buildreq on Tue Mar 16 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Create usable views in Ruby with HTML and CSS selectors.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%package -n rails-plugin-%plugname
Summary: Rails plugin for %name
Group: Development/Ruby
Requires: ruby-%plugname

%description  -n rails-plugin-%plugname
Rails plugin for %name

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
mkdir -p %buildroot%_datadir/rails/plugins/%plugname
%ruby_install
install -p -m644 rails/init.rb %buildroot%_datadir/rails/plugins/%plugname/
%rdoc lib/

%files
%doc README.textile TODO.textile
%ruby_sitelibdir/*

%files -n rails-plugin-%plugname
%_datadir/rails/plugins/%plugname

%files doc
%ruby_ri_sitedir/Effigy*

%changelog
* Tue Mar 16 2010 Timur Batyrshin <erthad@altlinux.org> 0.3.1-alt1
- Built for Sisyphus
