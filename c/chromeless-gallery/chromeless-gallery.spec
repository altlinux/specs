Name: chromeless-gallery
# The version is the average version of the components.
Version: 0.16
Release: alt1

Summary: A set of advanced example applications for the Cheomeless platform
License: MPL 1.1/GPL 2.0+/LGPL 2.1+, Apache 2.0, MIT
Group: Networking/WWW
Url: https://github.com/mozilla/chromeless/tree/master/gallery

Packager: Paul Wolneykien <manowar@altlinux.ru>
Source: %name-%version.tar

Requires: chromeless

BuildArch: noarch

%description
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

This package provides some advanced example applications built on
a top of the platform. More examples, including the Webian Shell,
can be found in separate packages.

%define gallery %_datadir/chromeless/gallery
%define _docdir %_datadir/doc/%name-%version

%prep
%setup

%install
mkdir -m0755 -p %buildroot%gallery
cp -R --preserve=mode,timestamps * %buildroot%gallery/
pushd %buildroot%gallery
for d in *; do mkdir -p -m0755 "%buildroot%_docdir/$d"; cd "$d"; mv *.md "%buildroot%_docdir/$d/"; cd ..; done
popd

%files
%gallery
%dir %_docdir
%dir %_docdir/*
%doc %_docdir/*/*.md

%changelog
* Wed Jul 13 2011 Paul Wolneykien <manowar@altlinux.ru> 0.16-alt1
- simple text editor changes:
  + Contributor Julian and the save new file (thx Marcio Galli).
  + Check if the user selected a file (thx Julian Viereck).
  + Add worker-javascript.js file to enable JavaScript validation
    (thx Julian Vierec).
  + Add welcome message to index.html (thx Julian Viereck).
  + Add index.js file. Reuse the editor by setting the value on
    the editSession (thx Julian Viereck).
  + Edited index.html via GitHub (thx ironfroggy).
  + fix non sys priv and menu changes (thx Marcio Galli).
  + Fixes to the menu (thx Marcio Galli).
  + Ace Editor Documentation (thx Marcio Galli).
  + Fixes to have File Open and File save (thx Marcio Galli).
  + Ace and initial HTML launching Ace simplified. (thx Marcio Galli).
- ereader-transcoder changes:
  + polish , when save it auto updates the catalog on the left
    (thx Marcio Galli).
  + config scroll fix (thx Marcio Galli).
  + E-reader UI (thx Marcio Galli).
  + Reorg cleanup and main vs skin (thx Marcio Galli).
  + Docs (thx Marcio Galli).
  + Doc (thx Marcio Galli).
  + Reorg basc (thx Marcio Galli).
  + Fixup to new require('fs') and file save (thx Marcio Galli).
  + New layout and polish to UI elements (thx Marcio Galli).
  + Hidden scrollbars (thx Marcio Galli).
  + Inverting the scroll, experimental and breaks the DOM events,
    prevents and directly sets (thx Marcio Galli).
  + Catalog list on the left, soon to be drag out and in.
    (thx Marcio Galli).
  + Fixes workaround so it works in Chromeless. Looks like Chromeless
    cannot see the StyleSheets (thx Marcio Galli).
  + Webby Browser, from Chromeless examples, with Readability 3rd-party
    API and functions to save and revel directory. (thx Marcio Galli).
- focusTimer changes:
  + Fix link to icon (thx Dan Mosedale).
  + Another attempt to unhork the markdown (thx Dan Mosedale).
  + Fix markdown bustage (thx Dan Mosedale).
  + Fixed fluid instructions; thanks to anant for noticing the bustage.
    (thx Dan Mosedale).
  + Update version in appinfo for chromless users (thx Dan Mosedale).
  + Cleanup markdown (thx Dan Mosedale).
  + Made roadmap sane (thx Dan Mosedale).
  + Split apart ChangeLog & roadmap (thx Dan Mosedale).
  + Hackery warning message (thx Dan Mosedale).
  + Get favicon working (thx Dan Mosedale).
  + Clarified text about why manual setup is necessary.
    (thx Dan Mosedale).
  + Add a favicon with 3 sizes (thx Dan Mosedale).
  + Documentation / roadmap updates (thx Dan Mosedale).
  + Added .gitignore and .project files (thx Dan Mosedale).
  + A bunch of documentation cleanup (thx Dan Mosedale).
  + rename to focusTimer (thx Dan Mosedale).
  + Some more variable rename fixery. (thx Dan Mosedale).
  + Draft basic instructions for using with fluid; fix more variable
    name change bugs. (thx Dan Mosedale).
  + Added appinfo.json for experimental chromeless support
    (thx Dan Mosedale).
  + Fixed some bugs caused by an incomplete variable rename
    (thx Dan Mosedale).
  + Fixed now obsolete include of jqTimer.js (thx Dan Mosedale).
  + Cleaned up the roadmap and moved a bunch of stuff around in
    preparation for creating a simple building process for a Fluid app
    (thx Dan Mosedale).
  + Added credits section + licensing info to the README; updated
    the roadmap. (thx Dan Mosedale).
  + Various code + roadmap cleanup (thx Dan Mosedale).
  + Tweak to run in both fluid.app and browser contexts; make grey
    paused state work; update roadmap (thx Dan Mosedale).
  + Tweak a comment, and massage the roadmap (thx Dan Mosedale).
  + Esthetic cleanups + roadmap massage (thx Dan Mosedale).
  + Removed old version of jQuery (thx Dan Mosedale).
  + Clarify roadmap (thx Dan Mosedale).
  + Update style on text field itself (thx Dan Mosedale).
  + Clarify roadmap (thx Dan Mosedale).
  + Change default white to green (thx Dan Mosedale).
  + Ditch gratuitous use of seconds on buttons (thx Dan Mosedale).
  + Update the roadmap (thx Dan Mosedale).
  + Get styling working and make a few tweaks (thx Dan Mosedale).
  + Fix indenting and actually include the jQuery UI CSS so that we
    get some style (thx Dan Mosedale).
  + Update roadmap (thx Dan Mosedale).
  + Hide the pause/run button when the timer has run out; reset
    otherwise. (thx Dan Mosedale).
  + Updated roadmap. (thx Dan Mosedale).
  + A few markdown tweaks. (thx Dan Mosedale).
  + Added a simple README file. (thx Dan Mosedale).
  + initial commit (thx Dan Mosedale).

