%global with_tests %nil

%ifarch %ix86
%global with_tests -f
%endif

Name:           flexmark-java
Version:        0.64.6
Release:        alt1

Summary:        CommonMark/Markdown Java parser with source level AST
License:        BSD-2-Clause
Group:          Development/Java
URL:            https://github.com/vsch/flexmark-java
VCS:            https://github.com/vsch/flexmark-java

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jetbrains:annotations)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.nibor.autolink:autolink)
BuildRequires:  mvn(org.jsoup:jsoup)

BuildArch:      noarch

%description
flexmark-java is a Java implementation of CommonMark (spec 0.28) parser using
the blocks first, inlines after Markdown parsing architecture.

Its strengths are speed, flexibility, Markdown source element based AST with
details of the source position down to individual characters of lexemes that
make up the element and extensibility.

The API allows granular control of the parsing process and is optimized for
parsing with a large number of installed extensions. The parser and extensions
come with plenty of options for parser behavior and HTML rendering variations.
The end goal is to have the parser and renderer be able to mimic other parsers
with great degree of accuracy. This is now partially complete with the
implementation of Markdown Processor Emulation.

%javadoc_package

%package        all
Summary:        All flexmark extension and converter modules
Group:          Development/Java

%description    all
%summary.

%package        ext-abbreviation
Summary:        Flexmark-java extension for abbreviations in text
Group:          Development/Java

%description    ext-abbreviation
Flexmark-java extension for defining abbreviations and turning appearance of
these abbreviations in text into links with titles consisting of the expansion
of the abbreviation.

%package        ext-admonition
Summary:        Flexmark-java extension for admonition syntax
Group:          Development/Java

%description    ext-admonition
%summary.

%package        ext-anchorlink
Summary:        Flexmark-java extension to generate anchor links for headers
Group:          Development/Java

%description    ext-anchorlink
Flexmark-java extension for generating anchor links for headings using GitHub
compatible algorithm.

%package        ext-aside
Summary:        Flexmark-java extension for converting | to aside tags
Group:          Development/Java

%description    ext-aside
%summary.

%package        ext-attributes
Summary:        Flexmark-java extension for attributes
Group:          Development/Java

%description    ext-attributes
%summary.

%package        ext-autolink
Summary:        Flexmark-java extension for autolinking
Group:          Development/Java

%description    ext-autolink
Flexmark-java extension for turning plain URLs and email addresses into links.

%package        ext-definition
Summary:        Flexmark-java extension for definition
Group:          Development/Java

%description    ext-definition
%summary.

%package        ext-emoji
Summary:        Flexmark-java extension for emoji shortcuts
Group:          Development/Java

%description    ext-emoji
Flexmark-java extension for emoji shortcuts using Emoji-Cheat-Sheet.com.

%package        ext-enumerated-reference
Summary:        Flexmark-java extension for enumerated reference
Group:          Development/Java

%description    ext-enumerated-reference
Flexmark-java extension for enumerated reference processing.

%package        ext-escaped-character
Summary:        Flexmark-java extension for escaped_character
Group:          Development/Java

%description    ext-escaped-character
%summary.

%package        ext-footnotes
Summary:        Flexmark-java extension for footnotes
Group:          Development/Java

%description    ext-footnotes
Flexmark-java extension for footnote inline elments and footnote definitions.

%package        ext-gfm-issues
Summary:        Flexmark-java extension for GitHub issue syntax
Group:          Development/Java

%description    ext-gfm-issues
Flexmark-java extension for GitHub issue syntax.

%package        ext-gfm-strikethrough
Summary:        Flexmark-java extension for strikethrough
Group:          Development/Java

%description    ext-gfm-strikethrough
Flexmark-java extension for GFM strikethrough
using ~~ (GitHub Flavored Markdown).

%package        ext-gfm-tasklist
Summary:        Flexmark-java extension for generating GitHub style task list items
Group:          Development/Java

%description    ext-gfm-tasklist
Flexmark-java extension to convert bullet list items that start with [ ] to
a TaskListItem node.

%package        ext-gfm-users
Summary:        Flexmark-java extension for GitHub user syntax
Group:          Development/Java

%description    ext-gfm-users
%summary.

%package        ext-gitlab
Summary:        Flexmark-java extension for GitLab Flavoured Markdown
Group:          Development/Java

%description    ext-gitlab
%summary.

%package        ext-ins
Summary:        Flexmark-java extension for ins
Group:          Development/Java

%description    ext-ins
%summary.

%package        ext-jekyll-front-matter
Summary:        Flexmark-java extension for jekyll_front_matter
Group:          Development/Java

%description    ext-jekyll-front-matter
%summary.

%package        ext-jekyll-tag
Summary:        Flexmark-java extension for jekyll tag parsing
Group:          Development/Java

%description    ext-jekyll-tag
%summary.

%package        ext-macros
Summary:        Flexmark-java extension for processing macros
Group:          Development/Java

%description    ext-macros
%summary.

%package        ext-media-tags
Summary:        Flexmark-java extension for HTML5 media tags
Group:          Development/Java

%description    ext-media-tags
Flexmark-java extension parsing and rendering HTML5 media tags.

%package        ext-resizable-image
Summary:        Flexmark-java extension for image's size
Group:          Development/Java

%description    ext-resizable-image
Flexmark-java extension to set the size of the images.

%package        ext-spec-example
Summary:        Flexmark-java extension for specexample
Group:          Development/Java

%description    ext-spec-example
%summary.

%package        ext-superscript
Summary:        Flexmark-java extension for superscript
Group:          Development/Java

%description    ext-superscript
%summary.

%package        ext-tables
Summary:        Flexmark-java extension for tables
Group:          Development/Java

%description    ext-tables
Flexmark-java extension for tables using "|" pipes with optional column spans
and table caption.

%package        ext-toc
Summary:        Flexmark-java extension for toc
Group:          Development/Java

%description    ext-toc
%summary.

%package        ext-typographic
Summary:        Flexmark-java extension for typographic
Group:          Development/Java

%description    ext-typographic
%summary.

%package        ext-wikilink
Summary:        Flexmark-java extension for wiki links
Group:          Development/Java

%description    ext-wikilink
Flexmark-java extension parsing and rendering wiki links

%package        ext-xwiki-macros
Summary:        Flexmark-java extension for xwiki application specific macros
Group:          Development/Java

%description    ext-xwiki-macros
%summary.

%package        ext-yaml-front-matter
Summary:        Flexmark-java extension for YAML front matter
Group:          Development/Java

%description    ext-yaml-front-matter
%summary.

%package        ext-youtube-embedded
Summary:        Flexmark extension for YouTube links
Group:          Development/Java

%description    ext-youtube-embedded
%summary.

%package        ext-zzzzzz
Summary:        Flexmark-java extension for zzzzzz
Group:          Development/Java

%description    ext-zzzzzz
%summary.

%package        html2md-converter
Summary:        Flexmark-java HTML to Markdown extensible converter
Group:          Development/Java

%description    html2md-converter
Flexmark-java customizable extension to convert HTML to Markdown.

%package        integration-test
Summary:        Flexmark-java integration tests
Group:          Development/Java

%description    integration-test
Tests integration of all extensions.

%package        jira-converter
Summary:        Flexmark-java extension for jira_converter
Group:          Development/Java

%description    jira-converter
%summary.

%package        osgi
Summary:        Flexmark OSGi bundle
Group:          Development/Java

%description    osgi
Flexmark-java core osgi bundle, all extension modules and converter modules
except PDF converter in the OSGi Bundle format.

%package        test-specs
Summary:        Flexmark-java test spec files
Group:          Development/Java

%description    test-specs
Flexmark-java CommonMark specs for tests.

%package        test-util
Summary:        Flexmark-java test utilities
Group:          Development/Java

%description    test-util
Flexmark-java classes for tests.

%package        tree-iteration
Summary:        Flexmark-java library for recursive tree iteration
Group:          Development/Java

%description    tree-iteration
Flexmark-java library for recursive tree iteration with the filtering
and recursion conditions provided by predicates.

%package        util-ast
Summary:        Flexmark-java ast utilities
Group:          Development/Java

%description    util-ast
Flexmark-java ast utility classes.

%package        util-builder
Summary:        Flexmark-java builder utilities
Group:          Development/Java

%description    util-builder
Flexmark-java builder utility classes.

%package        util-collection
Summary:        Flexmark-java collection utilities
Group:          Development/Java

%description    util-collection
Flexmark-java collection utility classes.

%package        util-data
Summary:        Flexmark-java data utilities
Group:          Development/Java

%description    util-data
Flexmark-java collection data utility classes.

%package        util-dependency
Summary:        Flexmark-java dependency utilities
Group:          Development/Java

%description    util-dependency
Flexmark-java dependency utility classes.

%package        util-experimental
Summary:        Flexmark-java experimental utility classes
Group:          Development/Java

%description    util-experimental
Contains experimental classes that may or may not work in all cases.
Use at your own risk.

%package        util-format
Summary:        Flexmark-java format utilities
Group:          Development/Java

%description    util-format
Flexmark-java format utility classes.

%package        util-html
Summary:        Flexmark-java html utilities
Group:          Development/Java

%description    util-html
Flexmark-java html utility classes.

%package        util-misc
Summary:        Flexmark-java misc utilities
Group:          Development/Java

%description    util-misc
Flexmark-java misc utility classes.

%package        util-options
Summary:        Flexmark-java options utilities
Group:          Development/Java

%description    util-options
Flexmark-java options utility classes.

%package        util-sequence
Summary:        Flexmark-java sequence utilities
Group:          Development/Java

%description    util-sequence
Flexmark-java sequence utility classes.

%package        util-visitor
Summary:        Flexmark-java visitor utilities
Group:          Development/Java

%description    util-visitor
Flexmark-java visitor utility classes.

%package        util
Summary:        Flexmark-java utilities
Group:          Development/Java

%description    util
Flexmark-java utility classes.

%package        youtrack-converter
Summary:        Flexmark-java extension for YouTrack conversion
Group:          Development/Java

%description    youtrack-converter
%summary.

%prep
%setup

rm flexmark-util/src/test/java/com/vladsch/flexmark/util/html/ui/HtmlBuilderTest.java
rm flexmark-util/src/test/java/com/vladsch/flexmark/util/html/HtmlTestSuite.java
rm flexmark-util/src/test/java/com/vladsch/flexmark/util/UtilTestSuite.java

%pom_remove_dep -r org.pegdown:pegdown
rm flexmark-integration-test/src/test/java/com/vladsch/flexmark/integration/test/PegDownBenchmark.java

# Disable due to missing openhtmltopdf dependency
%pom_disable_module flexmark-pdf-converter
%pom_disable_module flexmark-profile-pegdown
%pom_disable_module flexmark-docx-converter

%pom_remove_dep :flexmark-profile-pegdown flexmark-all
%pom_remove_dep :flexmark-profile-pegdown flexmark-osgi
%pom_remove_dep :flexmark-pdf-converter flexmark-all

%build
%mvn_build -s %with_tests

%install
%mvn_install

for m in core-test integration-test test-specs; do
  rm %buildroot%_javadir/flexmark-java/flexmark-$m.jar
  rm %buildroot%_mavenpomdir/flexmark-java/flexmark-$m.pom
  rm %buildroot%_datadir/maven-metadata/flexmark-java-flexmark-$m.xml
done

%files -f .mfiles-flexmark-java -f .mfiles-flexmark
%_datadir/maven-metadata/flexmark-java-flexmark-java.xml
%_mavenpomdir/flexmark-java/flexmark-java.pom
%doc README.md LICENSE.txt

%files all -f .mfiles-flexmark-all

%files ext-abbreviation -f .mfiles-flexmark-ext-abbreviation

%files ext-admonition -f .mfiles-flexmark-ext-admonition

%files ext-anchorlink -f .mfiles-flexmark-ext-anchorlink

%files ext-aside -f .mfiles-flexmark-ext-aside

%files ext-attributes -f .mfiles-flexmark-ext-attributes

%files ext-autolink -f .mfiles-flexmark-ext-autolink

%files ext-definition -f .mfiles-flexmark-ext-definition

%files ext-emoji -f .mfiles-flexmark-ext-emoji

%files ext-enumerated-reference -f .mfiles-flexmark-ext-enumerated-reference

%files ext-escaped-character -f .mfiles-flexmark-ext-escaped-character

%files ext-footnotes -f .mfiles-flexmark-ext-footnotes

%files ext-gfm-issues -f .mfiles-flexmark-ext-gfm-issues

%files ext-gfm-strikethrough -f .mfiles-flexmark-ext-gfm-strikethrough

%files ext-gfm-tasklist -f .mfiles-flexmark-ext-gfm-tasklist

%files ext-gfm-users -f .mfiles-flexmark-ext-gfm-users

%files ext-gitlab -f .mfiles-flexmark-ext-gitlab

%files ext-ins -f .mfiles-flexmark-ext-ins

%files ext-jekyll-front-matter -f .mfiles-flexmark-ext-jekyll-front-matter

%files ext-jekyll-tag -f .mfiles-flexmark-ext-jekyll-tag

%files ext-macros -f .mfiles-flexmark-ext-macros

%files ext-media-tags -f .mfiles-flexmark-ext-media-tags

%files ext-resizable-image -f .mfiles-flexmark-ext-resizable-image

%files ext-spec-example -f .mfiles-flexmark-ext-spec-example

%files ext-superscript -f .mfiles-flexmark-ext-superscript

%files ext-tables -f .mfiles-flexmark-ext-tables

%files ext-toc -f .mfiles-flexmark-ext-toc

%files ext-typographic -f .mfiles-flexmark-ext-typographic

%files ext-wikilink -f .mfiles-flexmark-ext-wikilink

%files ext-xwiki-macros -f .mfiles-flexmark-ext-xwiki-macros

%files ext-yaml-front-matter -f .mfiles-flexmark-ext-yaml-front-matter

%files ext-youtube-embedded -f .mfiles-flexmark-ext-youtube-embedded

%files ext-zzzzzz -f .mfiles-flexmark-ext-zzzzzz

%files html2md-converter -f .mfiles-flexmark-html2md-converter

%files jira-converter -f .mfiles-flexmark-jira-converter

%files osgi -f .mfiles-flexmark-osgi

%files test-util -f .mfiles-flexmark-test-util

%files tree-iteration -f .mfiles-flexmark-tree-iteration
%doc flexmark-tree-iteration/README.md flexmark-tree-iteration/LICENSE.txt

%files util -f .mfiles-flexmark-util

%files util-ast -f .mfiles-flexmark-util-ast

%files util-builder -f .mfiles-flexmark-util-builder

%files util-collection -f .mfiles-flexmark-util-collection

%files util-data -f .mfiles-flexmark-util-data

%files util-dependency -f .mfiles-flexmark-util-dependency

%files util-experimental -f .mfiles-flexmark-util-experimental

%files util-format -f .mfiles-flexmark-util-format

%files util-html -f .mfiles-flexmark-util-html

%files util-misc -f .mfiles-flexmark-util-misc

%files util-options -f .mfiles-flexmark-util-options

%files util-sequence -f .mfiles-flexmark-util-sequence

%files util-visitor -f .mfiles-flexmark-util-visitor

%files youtrack-converter -f .mfiles-flexmark-youtrack-converter

%changelog
* Sun Apr 05 2026 Evgeniy Serov <scala@altlinux.org> 0.64.6-alt1
- Initial build for Sisyphus.
