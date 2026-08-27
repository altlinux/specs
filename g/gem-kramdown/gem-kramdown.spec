# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname kramdown

Name:          gem-kramdown
Version:       2.5.2
Release:       alt1
Summary:       kramdown is a fast, pure Ruby Markdown superset converter
License:       MIT
Group:         Development/Ruby
Url:           http://kramdown.gettalong.org
Vcs:           https://github.com/gettalong/kramdown.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rexml) >= 3.4.4
BuildRequires: gem(rouge) >= 3.26.0
BuildRequires: gem(stringex) >= 1.5.1
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rouge) >= 4
BuildConflicts: gem(stringex) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency stringex >= 2.8.0,stringex < 3
Requires:      ruby >= 2.5
Requires:      gem(rexml) >= 3.4.4
Provides:      gem(kramdown) = 2.5.2

%description
kramdown was originally licensed under the GPL until the 1.0.0 release. However,
due to the many requests it is now released under the MIT license and therefore
can easily be used in commercial projects, too.

kramdown is a fast, pure Ruby Markdown superset converter, using a strict syntax
definition and supporting several common extensions.

The syntax definition for the kramdown syntax can be found in doc/syntax.page
(or online at http://kramdown.gettalong.org/syntax.html) and a quick reference
is available in doc/quickref.page or online at
http://kramdown.gettalong.org/quickref.html.

The kramdown library is mainly written to support the kramdown-to-HTML
conversion chain. However, due to its flexibility (by creating an internal AST)
it supports other input and output formats as well. Here is a list of the
supported formats:

* input formats: kramdown (a Markdown superset), Markdown, GFM, HTML
* output formats: HTML, kramdown, LaTeX (and therefore PDF), PDF via Prawn

All the documentation on the available input and output formats is available in
the doc/ directory and online at http://kramdown.gettalong.org.

Starting from version 1.0.0 kramdown is using a versioning scheme with major,
minor and patch parts in the version number where the major number changes on
backwards-incompatible changes, the minor number on the introduction of new
features and the patch number on everything else.


%package       -n kramdown
Version:       2.5.2
Release:       alt1
Summary:       kramdown is a fast, pure Ruby Markdown superset converter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета kramdown
Group:         Other
BuildArch:     noarch

Requires:      gem(kramdown) = 2.5.2

%description   -n kramdown
kramdown is a fast, pure Ruby Markdown superset converter
executable(s).

kramdown was originally licensed under the GPL until the 1.0.0 release. However,
due to the many requests it is now released under the MIT license and therefore
can easily be used in commercial projects, too.

kramdown is a fast, pure Ruby Markdown superset converter, using a strict syntax
definition and supporting several common extensions.

The syntax definition for the kramdown syntax can be found in doc/syntax.page
(or online at http://kramdown.gettalong.org/syntax.html) and a quick reference
is available in doc/quickref.page or online at
http://kramdown.gettalong.org/quickref.html.

The kramdown library is mainly written to support the kramdown-to-HTML
conversion chain. However, due to its flexibility (by creating an internal AST)
it supports other input and output formats as well. Here is a list of the
supported formats:

* input formats: kramdown (a Markdown superset), Markdown, GFM, HTML
* output formats: HTML, kramdown, LaTeX (and therefore PDF), PDF via Prawn

All the documentation on the available input and output formats is available in
the doc/ directory and online at http://kramdown.gettalong.org.

Starting from version 1.0.0 kramdown is using a versioning scheme with major,
minor and patch parts in the version number where the major number changes on
backwards-incompatible changes, the minor number on the introduction of new
features and the patch number on everything else.

%description   -n kramdown -l ru_RU.UTF-8
Исполнямка для самоцвета kramdown.


%if_enabled    doc
%package       -n gem-kramdown-doc
Version:       2.5.2
Release:       alt1
Summary:       kramdown is a fast, pure Ruby Markdown superset converter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kramdown
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kramdown) = 2.5.2

%description   -n gem-kramdown-doc
kramdown is a fast, pure Ruby Markdown superset converter documentation
files.

kramdown was originally licensed under the GPL until the 1.0.0 release. However,
due to the many requests it is now released under the MIT license and therefore
can easily be used in commercial projects, too.

kramdown is a fast, pure Ruby Markdown superset converter, using a strict syntax
definition and supporting several common extensions.

The syntax definition for the kramdown syntax can be found in doc/syntax.page
(or online at http://kramdown.gettalong.org/syntax.html) and a quick reference
is available in doc/quickref.page or online at
http://kramdown.gettalong.org/quickref.html.

The kramdown library is mainly written to support the kramdown-to-HTML
conversion chain. However, due to its flexibility (by creating an internal AST)
it supports other input and output formats as well. Here is a list of the
supported formats:

* input formats: kramdown (a Markdown superset), Markdown, GFM, HTML
* output formats: HTML, kramdown, LaTeX (and therefore PDF), PDF via Prawn

All the documentation on the available input and output formats is available in
the doc/ directory and online at http://kramdown.gettalong.org.

Starting from version 1.0.0 kramdown is using a versioning scheme with major,
minor and patch parts in the version number where the major number changes on
backwards-incompatible changes, the minor number on the introduction of new
features and the patch number on everything else.

%description   -n gem-kramdown-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kramdown.
%endif


%if_enabled    devel
%package       -n gem-kramdown-devel
Version:       2.5.2
Release:       alt1
Summary:       kramdown is a fast, pure Ruby Markdown superset converter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kramdown
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kramdown) = 2.5.2
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rouge) >= 3.26.0
Requires:      gem(stringex) >= 1.5.1
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rouge) >= 4
Conflicts:     gem(stringex) >= 3

%description   -n gem-kramdown-devel
kramdown is a fast, pure Ruby Markdown superset converter development
package.

kramdown was originally licensed under the GPL until the 1.0.0 release. However,
due to the many requests it is now released under the MIT license and therefore
can easily be used in commercial projects, too.

kramdown is a fast, pure Ruby Markdown superset converter, using a strict syntax
definition and supporting several common extensions.

The syntax definition for the kramdown syntax can be found in doc/syntax.page
(or online at http://kramdown.gettalong.org/syntax.html) and a quick reference
is available in doc/quickref.page or online at
http://kramdown.gettalong.org/quickref.html.

The kramdown library is mainly written to support the kramdown-to-HTML
conversion chain. However, due to its flexibility (by creating an internal AST)
it supports other input and output formats as well. Here is a list of the
supported formats:

* input formats: kramdown (a Markdown superset), Markdown, GFM, HTML
* output formats: HTML, kramdown, LaTeX (and therefore PDF), PDF via Prawn

All the documentation on the available input and output formats is available in
the doc/ directory and online at http://kramdown.gettalong.org.

Starting from version 1.0.0 kramdown is using a versioning scheme with major,
minor and patch parts in the version number where the major number changes on
backwards-incompatible changes, the minor number on the introduction of new
features and the patch number on everything else.

%description   -n gem-kramdown-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kramdown.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n kramdown
%doc COPYING README.md
%_bindir/kramdown

%if_enabled    doc
%files         -n gem-kramdown-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-kramdown-devel
%doc COPYING README.md
%endif


%changelog
* Wed Jun 10 2026 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- ^ 2.3.1 -> 2.5.2

* Tue Oct 12 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt3
- ! to change stringex dep to runtime from devel

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt2
- ! spec
- ! loading Rakefile multiple times

* Thu Mar 25 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.3.1-alt1
- New version.

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
