Name:    ronn
Version: 0.7.3
Release: alt1

Summary: Ronn builds manuals from Markdown to roff format
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rtomayko/ronn/

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-hpricot
BuildRequires: rdiscount
BuildRequires: mustache

%description
Ronn builds manuals. It converts simple, human readable textfiles to
roff for terminal display, and also to HTML for the web. The source
format includes all of Markdown but has a more rigid structure and
syntax extensions for features commonly found in manpages (definition
lists, link notation, etc.). The ronn-format(7) manual page defines the
format in detail.

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

# Clean source files amd put man page to appropriate directories
rm -f %buildroot%_mandir/index.*
rm -f %buildroot%_mandir/*.ronn
mkdir -p %buildroot%_man1dir
mv %buildroot%_mandir/*.1* %buildroot%_man1dir
mkdir -p %buildroot%_man7dir
mv %buildroot%_mandir/*.7* %buildroot%_man7dir

%check
chmod +x bin/ronn
%ruby_test_unit -Ilib:test test/test*.rb

%files
%doc README*
%_bindir/%name
%ruby_sitelibdir/*
%_man1dir/*.1*
%_man7dir/*.7*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
