%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:	A python library for manipulating kickstart files
Name:		pykickstart
Version:	1.99.15
Release:	8
License:	GPLv2
Group:		Development/Python
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Url:		http://fedoraproject.org/wiki/pykickstart
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
Requires:	python
Requires:	python-urlgrabber

%description
The pykickstart package is a python library for manipulating kickstart
files.

%prep
%setup -q

%build
make

%install
make DESTDIR=%{buildroot} install
%find_lang %{name}

%files -f %{name}.lang
%doc README ChangeLog COPYING docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python_sitelib}/*
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff

