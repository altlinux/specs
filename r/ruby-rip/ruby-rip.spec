%define pkgname rip

Name: ruby-%pkgname
Version: 0.0.5
Release: alt1

Summary: Installs and manages RubyGems, git repositories, and more.
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/defunkt/rip

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-setup 

# these buildreqs are required for tests only
#BuildRequires: git-server ruby-rake /proc

%description
Like virtualenv + pip for Ruby.

Installs and manages RubyGems, git repositories, and more.

We're currently in a developer-mode rewrite: rip2.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

#%%check
# tests do not work in hasher so run these yourself with the following comand
# PATH="$PATH:/usr/sbin" rake test

%install
%ruby_install

%files
%doc README.markdown
%ruby_sitelibdir/*
%_bindir/*

%changelog
* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.5-alt1
- New version

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.0.0.20100616-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Jun 27 2010 Timur Batyrshin <erthad@altlinux.org> 0.0.0.20100616-alt2
- removed excess usage of __FILE__

* Sun Jun 27 2010 Timur Batyrshin <erthad@altlinux.org> 0.0.0.20100616-alt1
- Built for Sisyphus

