
const colors = require('colors/safe')
const { argv, exit} = require('process')
const Kahoot = require('kahoot.js-updated')
const fs = require('fs')
const config = require('./config.json')

if (argv.length === 4) {
    var kahoot_game = argv[2]
    var amount = argv[3]
    console.log(`=== Attempting to join "${colors.green(kahoot_game)}" ${colors.yellow(amount.toString())} times ===`)
    for (let x = 0; x < amount; x++) {
        const client = new Kahoot();
        const username = config.usernames[Math.floor(Math.random() * config.usernames.length)] + Math.floor(Math.random() * 3003) ;
        client.join(kahoot_game, username)
        .then(() => {console.log(`--- Joined "${colors.green(kahoot_game)}" with bot: "${username}" ---`)})
        .catch(e => {console.error(e.description)})
    }
    console.log('Press CTRL + C to exit. [THIS WILL MAKE THE BOTS LEAVE]')
} else {
    console.log(`Usage:`)
    console.log(`   ${colors.green("node")} ${colors.cyan(__filename)} <${colors.yellow("invite")}> <${colors.yellow("amount")}>`)
    console.log(`   invite: ${colors.magenta('Invite code to the Kahoot game.')}`)
    console.log(`   amount: ${colors.magenta('Amount of times to join.')}`)
}
