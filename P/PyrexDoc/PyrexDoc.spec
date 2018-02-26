Name: PyrexDoc
Version: 0.1
Release: alt1.1
Summary: PyrexDoc - doco generator for Pyrex
License: Public domain
Group: Development/Python
Url: http://www.freenet.org.nz/python/pyrexdoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# https://codespeak.net/svn/py/dist
Source: %name-%version.tar.gz

%description
Pyrex has to be one of the greatest pieces of software since Python
itself.

In case you don't yet know, Pyrex is a language that lets you mix Python
and C code and data types freely. For that unavoidable chore of writing
Python wrappers to C libraries, Pyrex makes this task vastly quicker and
easier than with tools like SWIG.

Pyrex has many many uses including:

  * Easy creation of C library wrappers
  * Huge speed gains, by writing time-critical code with C syntax and C datatypes
  * All other situations where easy calling of C code is of help

The only problem with Pyrex is that the automatic documentation
generation tools, like epydoc, happydoc and pydoc, are unable to detect
functions, classes and class methods in Pyrex modules.

So, rather than hacking around inside any of these utilities, it worked
out quicker for me to write another documentation generator, especially
for Pyrex.

PyrexDoc is pretty basic, but generates perfectly usable documentation
by lifting docstrings out of built Pyrex modules.

%prep
%setup

%install
install -d %buildroot%_bindir
install -p -m755 pyrexdoc.py %buildroot%_bindir
ln -s pyrexdoc.py %buildroot%_bindir/pyrexdoc

%files
%_bindir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Tue Feb 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

