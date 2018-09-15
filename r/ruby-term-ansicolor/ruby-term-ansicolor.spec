Name: ruby-term-ansicolor
Version: 1.6.0
Release: alt1

Summary: Ruby library that colors strings using ANSI escape sequences
Group: Development/Ruby
License: GPLv2
Url: http://flori.github.io/term-ansicolor/

Source0: term-ansicolor-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-ruby

%description
Ruby library that colors strings using ANSI escape sequences.

%prep
%setup -q -n term-ansicolor-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc CHANGES README* examples
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*

%changelog
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.2
- Rebuild for new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 25 2009 Igor Zubkov <icesik@altlinux.org> 1.0.4-alt1
- build for Sisyphus

