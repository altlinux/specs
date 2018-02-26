%define plugname redhillonrails_core

Name: rails-plugin-%plugname
Version: 2.1.r355
Release: alt2

Summary: RedHill on Rails Core plugin for Ruby on Rails
Group: Development/Ruby
License: MIT
Url: http://www.redhillonrails.org/redhillonrails_core.html

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %plugname-%version.tar
Patch: %name-%version-%release.patch

PreReq: ruby-railties >= 2.1.0-alt2

# Automatically added by buildreq on Sat Aug 02 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-setup

%description
RedHill on Rails Core is a plugin that features to support
other RedHill on Rails plugins. Those features include:

 * Creating and dropping views;
 * Creating and removing foreign-keys;
 * Obtaining indexes directly from a model class; and
 * Determining when Schema.define() is running.

%prep
%setup -q -n %plugname-%version
%patch -p1
cp %_datadir/ruby-setup/setup.rb .

%build
%ruby_config --rbdir=%_datadir/rails/plugins/%plugname/lib
%ruby_build

%install
%ruby_install
install -p -m644 init.rb %buildroot%_datadir/rails/plugins/%plugname/
cp -dpR tasks/ %buildroot%_datadir/rails/plugins/%plugname/

%files
%doc CHANGELOG README
%_datadir/rails/plugins/%plugname

%changelog
* Sat Aug 02 2008 Sir Raorn <raorn@altlinux.ru> 2.1.r355-alt2
- Plugin code moved to plugin directory (Rails' module autoloading
  doesn't work with standard load paths)

* Sat Aug 02 2008 Sir Raorn <raorn@altlinux.ru> 2.1.r355-alt1
- Built for Sisyphus

