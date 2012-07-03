# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname rip

Name: ruby-%pkgname
Version: 0.0.0.20100616
Release: alt2

Summary: Installs and manages RubyGems, git repositories, and more.
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/defunkt/rip

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar

# Automatically added by buildreq on Sun Jun 27 2010 (-bi)
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
%doc README.md HISTORY.md
%ruby_sitelibdir/*
%_bindir/*
%_man1dir/*.gz
%_man5dir/*.gz

%changelog
* Sun Jun 27 2010 Timur Batyrshin <erthad@altlinux.org> 0.0.0.20100616-alt2
- removed excess usage of __FILE__

* Sun Jun 27 2010 Timur Batyrshin <erthad@altlinux.org> 0.0.0.20100616-alt1
- Built for Sisyphus

