/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                //Addin our custom color
                "site-gray-1": "#102A43",
                "site-gray-2": "#334E68",
                "site-gray-3": "#627D98",
                "site-gray-4": "#9FB3C8",
                "site-gray-5": "#c8dde3",
        
                "site-green-1": "#014D40",
                "site-green-2": "#147D64",
                "site-green-3": "#27AB83",
                "site-green-4": "#3EBD93",
                "site-green-5": "#8EEDC7",
        
                "site-white-1": "#abbbcb",
                "site-white-2": "#BCCCDC",
                "site-white-3": "#e0e4e8",
                "site-white-4": "#F0F4F8",
                "site-white-5": "#ffffff",
        
                "site-orange-1": "#841003",
                "site-orange-2": "#C52707",
                "site-orange-3": "#F35627",
                "site-orange-4": "#F9703E",
                "site-orange-5": "#FFB088",
        
                "site-yellow-1": "#8D2B0B",
                "site-yellow-2": "#CB6E17",
                "site-yellow-3": "#F0B429",
                "site-yellow-4": "#FADB5F",
                "site-yellow-5": "#FFF3C4",
              },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
