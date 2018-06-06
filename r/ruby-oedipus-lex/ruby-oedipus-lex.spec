%define  pkgname oedipus_lex

Name:    ruby-oedipus-lex
Version: 2.5.0
Release: alt1

Summary: This is not your father's lexer
License: MIT
Group:   Development/Ruby
Url:     https://github.com/seattlerb/oedipus_lex

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Provides: ruby-%pkgname = %EVR

%description
Oedipus Lex is a lexer generator in the same family as Rexical and Rex.
Oedipus Lex is my independent lexer fork of Rexical. Rexical was in turn
a fork of Rex. We've been unable to contact the author of rex in order
to take it over, fix it up, extend it, and relicense it to MIT. So,
Oedipus was written clean-room in order to bypass licensing constraints
(and because bootstrapping is fun).

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
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
* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
